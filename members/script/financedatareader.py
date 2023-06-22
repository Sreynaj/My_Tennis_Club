import base64
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
from io import BytesIO

def get_finance_data():
    # save figure to image
    df = fdr.DataReader('FRED:M2,NASDAQCOM,UMCSENT','2000')
    df.plot(secondary_y='UMCSENT')
    plt.savefig('image.png')
    #plt.show()

    # convert figure to image to base64
    #df = fdr.DataReader('FRED:M2,NASDAQCOM,UMCSENT','2000')
    #df.plot(secondary_y='UMCSENT')
    #pic_IObytes = BytesIO()
    #plt.savefig(pic_IObytes,  format='png')
    #pic_IObytes.seek(0)
    #pic_hash = base64.b64encode(pic_IObytes.read())
    #print(pic_hash)


    

get_finance_data()