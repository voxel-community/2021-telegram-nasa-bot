# Crea il tuo bot Telegram con i dati della NASA!

## Obiettivo di oggi

Imparare le basi di Python per creare un bot di Telegram che acceda ai dati sulle stelle della NASA 😊

Questo è un esempio di quello che potrete realizzare: [guarda qui]() 😉

---

## Com'è fatto un bot di Telegram?

### Python

Python è uno dei più popolari linguaggi di programmazione con cui sono state create tantissime funzionalità. Dall'algoritmo di raccomandazione film fino ai software che controllano le auto che si guidano da sole.

Python è un linguaggio di programmazione che è stato pensato per essere usato in diversi ambiti senza limiti, inclusi data science, software e sviluppo web, automazione e in generale per fare tante cose.

Oggi, con Python metteremo in comunicazione il bot di Telegram con i dati che ci fornisce la NASA.

A multi-purpose language with a simple, and beginner-friendly syntax

📹 [Ecco un breve video introduttivo](https://www.youtube.com/watch?v=Y8Tko2YC5hA)

### API

Le API sono programmi che consentono a due applicativi che parlano lingue diverse di interagire e dialogare e inoltre definiscono un contratto che suggella la promessa di espletare servizi su richiesta e in modo specifico.

Con le API, i siti web possono far fare agli utenti un gran numero di azioni, senza mai lasciare il sito web e senza far interagire gli utenti direttamente con il codice.

Con le API si possono far creare account, ricevere pagamenti o scaricare dati e informazioni. 

Ad esempio, le API della NASA che userai in questo workshop ti forniscono una lista di informazioni su stelle, pianeti e asteroidi.

📹 [Qui trovi un video breve su cosa sono le API](https://www.youtube.com/watch?v=OVvTv9Hy91Q)

## Struttura del workshop

Il workshop è strutturato in X capitoli, all'interno di ognuno troverai una breve guida su come realizzare un pezzettino del bot e un file contenente la soluzione che proponiamo noi riguardo ai capitoli precedenti. 

## Indice dei capitoli

00. [Installazione](00-installazione)
1. [Preparare il progetto](01-crea-bot)

--- 

## Potenziare il tuo sito 🚀

Una volta che avrai creato il tuo bot potrai potenziarlo e personalizzarlo ancora di più.

👉 Puoi cliccare qui per scoprire come fare: [Potenzia il tuo bot](potenzia-il-tuo-bot)

### Indice

- 

---

## Approfondimenti

👩🏻‍💻 Per ulteriori approfondimenti su Python, API e Telegram Bots ti consigliamo di visitare i seguenti siti:

-  Un corso gratuito della Università del Michigan su Python, [Python for Everybody](https://www.coursera.org/specializations/python)
- Python può essere usato anche per il lo sviluppo di applicazioni web, e c'è un corso a riguardo: [Django for Everybody Specialization](https://www.coursera.org/specializations/django)
- Scopri e impara come usare Python per le analisi dati, con il corso [IBM Data Analyst Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-analyst)
- Python può essere anche usato per automazioni e processi automatici e lo imparare vedere con il corso [Google IT Automation with Python Professional Certificate](https://www.coursera.org/professional-certificates/google-it-automation)
- Una lista di API di ogni tipo per arricchire i tuoi bot e altri tuoi progetti su [API List](https://apilist.fun/)

#### 👩🏻‍💻 Tutorial gratuiti:

- [FreeCodeCamp](https://www.freecodecamp.org/)
- [Codeacademy](https://www.codeacademy.com)
- [Khan Academy](https://it.khanacademy.org/computing/computer-programming/html-css)

Trovi maggiori informazioni su questo [articolo](https://www.voxel.community/it/-/blog/start-here) ✨

## Contatti

Se vuoi rimanere aggiornata sui nostri prossimi eventi, qui trovi i nostri contatti: 

### Voxel Community

🔵 Facebook: [@voxelcommunitytrento](https://www.facebook.com/voxelcommunitytrento)

🌐 Sito web: [https://www.voxel.community](https://www.voxel.community)

📧 Email: [hello@voxel.community](mailto:hello@voxel.community)

- https://tutorial.djangogirls.org/en/python_introduction/
- https://vercel.com/docs/concepts/functions/supported-languages#python
- https://www.marclittlemore.com/serverless-telegram-chatbot-vercel/
- https://core.telegram.org/bots/api#setwebhook
- https://xabaras.medium.com/setting-your-telegram-bot-webhook-the-easy-way-c7577b2d6f72

- https://api.telegram.org/botYOUR_TOKEN/getWebhookInfo

Webhooks are basically user defined HTTP callbacks (or small code snippets linked to a web application) which are triggered by specific events. Whenever that trigger event occurs in the source site, the webhook sees the event, collects the data, and sends it to the URL specified by you in the form of an HTTP request. You can even configure an event in one site to trigger an action in another site.

- https://snipcart.com/blog/what-are-webhooks-explained-example

Put bluntly: webhooks are a way for apps to communicate between them automatically.

MailChimp uses a webhook to signup users from your website to your newsletter.

Paypal uses it to tell your accounting app when your clients pay you.

Shopify offers webhooks to keep parts of your commerce system up-to-date, so you don’t have to enter new transaction details manually.

You can register a webhook by registering the URL to notify once given events occur. This first step is usually done via either a UI or by API.

HTTP web APIs
Endpoints
APIs provide you with an endpoint or a specific URL where the data or functions you want are exposed

https://www.culttt.com/2014/01/22/webhooks
### An API will request data

An API is an excellent way to communicate data between separate applications.
An API is basically a way to ask a question to another separate application. For example, if I was developing an application and I wanted my users to be able to find the people they follow on Twitter, I could ask the Twitter API, “Give me a list of all of the people this user follows on Twitter”.

An API is a common interface between two different applications. In the example above, it doesn’t make a difference if I write my application in Ruby and Twitter is written in Java because the API transmits and receives data in a common format (usually JSON or XML).
This allows two totally separate applications to send and receive data.

### A Webhook will receive data
So if an API is used to ask a question or make a direction request, what is a Webhook? A Webhook is basically a way to be notified when an event has occurred, usually not due to a direct action from your application.

For example, say I had created an application for my restaurant that used the Foursquare API to track when people checked in. When a user checks in with Foursquare I want to be able to greet them by name and offer them a complimentary drink.

If I was using an API I would have to be constantly asking “Is anyone here yet?” because if I didn’t ask the question I would never find out. This is very inefficient because my application would have to ask every couple of seconds and for the majority of the time the answer would probably be no.

A Webhook on the other hand would instead notify me when someone had checked in to my restaurant by sending me a request saying “Hey, Bob has just checked in”. This would allow me to run any processes I had in my application for such an event.

So an API is used to ask direct questions and a Webhook is used to be notified when certain events take place. Instead of constantly asking if anything has been changed, you can sit back and be notified when something actually has changed.

### Technically, what is a Webhook?

A Webhook is basically just a POST request that is sent to a specific URL. That URL is set up to receive the body of the POST request and process it in some way.
