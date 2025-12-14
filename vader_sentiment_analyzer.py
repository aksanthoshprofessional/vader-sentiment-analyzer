import tkinter as tk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def show_popup(sentiment, pos_score, neg_score, neu_score):
    popup = tk.Toplevel(window)
    popup.geometry('400x250')
    popup.configure(bg='#34495E')  
    title_label = tk.Label(popup, text="Sentiment Analysis Result", font=("Arial", 16, "bold"), bg='#34495E', fg='white')
    title_label.pack(pady=10)
    sentiment_label = tk.Label(popup, text=sentiment, font=("Arial", 14), bg='#34495E', fg='#F39C12') 
    sentiment_label.pack(pady=5)
    result_text = f" Positive Score: {pos_score:.2f}%\n Negative Score: {neg_score:.2f}%\n Neutral Score: {neu_score:.2f}%"
    scores_label = tk.Label(popup, text=result_text, font=("Arial", 12), bg='#34495E', fg='white')
    scores_label.pack(pady=10)
    close_btn = tk.Button(popup, text="Close", width=15, bg="#E74C3C", fg="white", font=("Arial", 12, "bold"), relief="raised", borderwidth=3, command=popup.destroy)
    close_btn.pack(pady=10)


def score():
    s = textArea.get("1.0", "end-1c")  
    vaderObj = SentimentIntensityAnalyzer()
    s_val = vaderObj.polarity_scores(s)
    if s_val['compound'] >= 0.05:
        sentiment = "Positive Sentiment"
    elif s_val['compound'] <= -0.05:
        sentiment = "Negative Sentiment"
    else:
        sentiment = "Neutral Sentiment"
    show_popup(sentiment, s_val['pos'] * 100, s_val['neg'] * 100, s_val['neu'] * 100)


window = tk.Tk()
window.geometry('600x300')
window.title('VADER Sentimental Analyzer')
window.configure(bg='#2C3E50')
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(2, weight=1)
custom_font = ('Arial', 14, 'bold')
button_style = {'width': 20, 'bg': '#E74C3C', 'fg': 'white', 'font': ('Arial', 12), 'relief': 'raised', 'borderwidth': 3}
label_1 = tk.Label(window, text="VADER Sentimental Analyzer", font=("Arial", 20, "bold"), bg='#2C3E50', fg='white')
label_1.grid(row=0, column=0, pady=10, sticky="n")
label_2 = tk.Label(window, text="Enter The Sentence Below", font=custom_font, bg='#2C3E50', fg='white')
label_2.grid(row=1, column=0, pady=5, sticky="n")
textArea = tk.Text(window, width=50, height=5, bg='white', fg='black', font=('Arial', 12), borderwidth=2, relief="solid")
textArea.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
b = tk.Button(window, text='Analyze', **button_style, command=score)
b.grid(row=3, column=0, pady=10)
window.mainloop()
