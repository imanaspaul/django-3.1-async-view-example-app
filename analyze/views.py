import httpx
from django.shortcuts import render


async def my_view(request):

    # IF GET REQUEST
    url = "https://text-sentiment.p.rapidapi.com/analyze"
    payload = "text=I want to kill you"

    headers = {
    'x-rapidapi-host': "text-sentiment.p.rapidapi.com",
    'x-rapidapi-key': "53023ab2bdmshb0d65b6b5f4664dp1aaaedjsn83e1a1d66f09",
    'content-type': "application/x-www-form-urlencoded"
    }

    r =  await httpx.AsyncClient().post(url, data=payload, headers=headers)
    pos_per = r.json().get("pos_percent")
    neg_per = r.json().get("neg_percent")
    mid_per = r.json().get("mid_percent")
    text = r.json().get("text")


    # IF POST REQUEST
    if request.method == 'POST':
        text = request.POST.get("text")
        payload = f"text={text}"
        r =  await httpx.AsyncClient().post(url, data=payload, headers=headers)
        pos_per = r.json().get("pos_percent")
        neg_per = r.json().get("neg_percent")
        mid_per = r.json().get("mid_percent")
        text = r.json().get("text")
        return render(request, 'analyze/index.html', {"pos_per": pos_per, "neg_per": neg_per, "mid_per": mid_per, "text": text })
    


    return render(request, 'analyze/index.html', {"pos_per": pos_per, "neg_per": neg_per, "mid_per": mid_per, "text": text })