from django.shortcuts import render, HttpResponse
import json


def index(request):
    return HttpResponse('Hello World!')

def primesUntill(request, offset):
    if request.method == 'GET':
        if not 'key' in request.GET:
            return HttpResponse("NO KEY WAS ENTERED!")

        json_string = json.dumps({"primes": primes(offset)}, indent=4)
        return HttpResponse(json_string)


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
