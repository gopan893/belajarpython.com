const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const axios = require('axios');

// Konfigurasi AI gratis (pakai API Gemini)
const GEMINI_API_KEY = "AIzaSyAWWn5y0N4xdsHMUzWfdV0gn7KPn-grnhE"; // Dapatkan dari makersuite.google.com/app/apikey

// Fungsi panggil AI
async function chatAI(pesan) {
    return "Test sukses. Kamu bilang: " + pesan;
}

// Inisialisasi client WhatsApp
const client = new Client({
    authStrategy: new LocalAuth(), // Simpan sesi agar tidak scan QR tiap kali
    puppeteer: { headless: true }
});

client.on('qr', (qr) => {
    console.log('Scan QR Code ini dengan WhatsApp:');
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('Bot WhatsApp siap!');
});

client.on('message', async (message) => {
    if (message.body.startsWith('!ai ')) {
        const pertanyaan = message.body.slice(4);
        const jawaban = await chatAI(pertanyaan);
        message.reply(jawaban);
    } else if (message.body === '!help') {
        message.reply('Gunakan !ai [pertanyaan] untuk chat dengan AI');
    }
});

client.initialize();