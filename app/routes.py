from flask import render_template, Response
from app import app
from analysis import final_start, final_end, final_distance, final_regular, df
import matplotlib.pyplot as plt
import io
import base64

@app.route('/')
@app.route('/index')
def index():

	img = io.BytesIO()

	duration_hist = df.hist(column='Duration', range=[0, 5000], bins=50, alpha=0.5)
	plt.savefig(img, format='png')
	img.seek(0)
	graph1_url = base64.b64encode(img.getvalue()).decode()
	plt.close()
	graph1_formatted_url = 'data:image/png;base64,{}'.format(graph1_url)

	passholder_pie = df['Passholder Type'].value_counts().plot(kind="pie")
	plt.savefig(img, format='png')
	img.seek(0)
	graph2_url = base64.b64encode(img.getvalue()).decode()
	plt.close()
	graph2_formatted_url = 'data:image/png;base64,{}'.format(graph2_url)

	distance_hist = df.hist(column='distance', range=[0, 4], bins=100, color='green', alpha=0.5)
	plt.savefig(img, format='png')
	img.seek(0)
	graph3_url = base64.b64encode(img.getvalue()).decode()
	plt.close()
	graph3_formatted_url = 'data:image/png;base64,{}'.format(graph3_url)

	return render_template('index.html', start=int(final_start[0][0]), end=int(final_end[0][0]), distance = final_distance, regular = final_regular[1], nonregular = final_regular[0], graph1 = graph1_formatted_url, graph2 = graph2_formatted_url, graph3 = graph3_formatted_url)
