from django.shortcuts import render
from .forms import DepositForm, ExtractionForm, TransferenceForm, ExchangeForm
from bankaccounts.models import BankAccount
from .models import HistorialObject
from decimal import Decimal
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def transactions_index(request):
    return render(request, 'transactions_index.html', {})

def transactions_deposit(request):
    form = DepositForm(request=request)

    context = {
        "form": form,
    }

    return render(request, 'transactions_deposit.html', context)

def transactions_depositsave(request):
    form = DepositForm(request.POST)
    bankaccount = BankAccount.objects.get(account_number=request.POST["account"])
    amount = request.POST["amount"]
    amount = Decimal(amount)

    context = {
        "bankaccount": bankaccount,
    }
    
    if form.is_valid():
        # import pdb; pdb.set_trace()
        bankaccount.balance += amount
        bankaccount.save()

        receipt = HistorialObject(
            account = bankaccount,
            amount = amount,
            transactiontype = "Deposit"
        )
        receipt.save()

        form.save()

        return render(request, 'bankaccounts_detail.html', context)
    else:
        print(form.errors)
        return HttpResponseRedirect('/bankaccounts/')

def transactions_extraction(request):
    form = ExtractionForm(request=request)
    context = {
        "form": form,
    }
    return render(request, 'transactions_extraction.html', context)

def transactions_extractionsave(request):
    form = ExtractionForm(request.POST)
    # import pdb; pdb.set_trace()
    bankaccount = BankAccount.objects.get(account_number=request.POST["account"])
    amount = request.POST["amount"]
    amount = Decimal(amount)

    if amount <= bankaccount.balance:
        bankaccount.balance -= amount
        bankaccount.save()

        receipt = HistorialObject(
            account = bankaccount,
            amount = amount,
            transactiontype = "Extraction")
        receipt.save()

        context = {
            "bankaccount": bankaccount,
            "amount": amount,
            "receipt": receipt,
        }
        
        if form.is_valid():
            form.save()
            return render(request, 'bankaccounts_detail.html', context)
        else:
            return render(request, 'bankaccounts_index.html', context)
        
    else:
            return render(request, 'transactions_extractionfail.html', context)

def transactions_exchange(request):
    form = ExchangeForm(request=request)
    context = {
        "form": form,
    }
    return render(request, 'transactions_exchange.html', context)

def transactions_exchangesave(request):
    form = ExchangeForm(request.POST)
    sender = BankAccount.objects.get(account_number=request.POST["sender"])
    receiver = BankAccount.objects.get(account_number=request.POST["receiver"])
    amount = request.POST["amount"]
    amount = Decimal(amount)
    conversion = 300

    context = {
    "form": form,
    "sender": sender,
    "receiver": receiver,
    "amount": amount,
    }

    if sender.account_number == receiver.account_number:
        return render(request, 'transactions_exchangesamenumber.html', context)

    elif sender.currency == receiver.currency:
        return render(request, 'transactions_exchangesamecurrency.html', context)
    
    elif amount > sender.balance:
        return render(request, 'transactions_exchangefail.html', context)

    elif amount <= sender.balance:
        if sender.currency == "ARS" and receiver.currency == "USD":
            sender.balance -= amount
            receiver.balance += amount / conversion
            converted = amount / conversion
            sender.save()
            receiver.save()

            receipt = HistorialObject(
                account = sender,
                amount = amount,
                transactiontype = "Exchange")
            receipt.save()

            context = {
            "form": form,
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "receipt": receipt,
            "conversion": conversion,
            "converted": converted,
            }

            if form.is_valid():
                form.save()
                return render(request, 'transactions_exchangesuccess.html', context)
            else:
                return render(request, 'transactions_index.html', context)
        
        elif sender.currency == "USD" and receiver.currency == "ARS":
            sender.balance -= amount
            receiver.balance += amount * conversion
            converted = amount * conversion
            sender.save()
            receiver.save()

            receipt = HistorialObject(
                account = sender,
                amount = amount,
                transactiontype = "Exchange")
            receipt.save()

            context = {
            "form": form,
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "receipt": receipt,
            "conversion": conversion,
            "converted": converted,
            }
            
            if form.is_valid():
                form.save()
                return render(request, 'transactions_exchangesuccess.html', context)
            else:
                return render(request, 'transactions_index.html', context)
            
def transactions_transference(request):
    form = TransferenceForm(request=request)
    context = {
        "form": form,
    }
    return render(request, 'transactions_transference.html', context)

def transactions_transferencesave(request):
    form = TransferenceForm(request.POST)
    sender = BankAccount.objects.get(account_number=request.POST["sender"])
    receiver = BankAccount.objects.get(account_number=request.POST["receiver"])
    amount = request.POST["amount"]
    amount = Decimal(amount)
    context = {
        "form": form,
        "sender": sender,
        "receiver": receiver,
        "amount": amount,
    }

    if sender.account_number == receiver.account_number:
        return render(request, 'transactions_transferencesamenumber.html', context)

    elif sender.currency != receiver.currency:
        return render(request, 'transactions_transferencesamecurrency.html', context)

    elif amount <= sender.balance:
        sender.balance -= amount
        receiver.balance += amount
        sender.save()
        receiver.save()

        receipt = HistorialObject(
            account = sender,
            amount = amount,
            transactiontype = "Transference")
        receipt.save()

        context = {
        "form": form,
        "sender": sender,
        "receiver": receiver,
        "amount": amount,
        "receipt": receipt,
        }

        if form.is_valid():
            form.save()
            return render(request, 'transactions_transferencesuccess.html', context)
        else:
            return render(request, 'bankaccounts_index.html', context)
    
    else:
        return render(request, 'transactions_transferencefail.html', context)