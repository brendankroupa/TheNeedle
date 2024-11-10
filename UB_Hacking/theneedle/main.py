from StarterGUI import get_url
from bias_counter import bias_stats
from summary import show_summary
from PercentageDandR import analyze_text_bias
from scraping import scraper
from data_reader import read_data

def main():
    # Step 1: Initialize and run the starter GUI to collect the URL
    url = get_url()  # Replace this with actual text input if needed
    scraped_text = scraper(url)
    # Step 2: Analyze text for bias
    result, percentage = analyze_text_bias('DandR.csv',scraped_text)  # Replace with actual CSV path
    temp = read_data('DandR.csv')
    bias_result = bias_stats(scraped_text, temp)
    # Step 3: Display the result in summary GUI
    show_summary(percentage, result, bias_result)
# NEED PERCENTAGE
if __name__ == "__main__":
    main()



    # https://go-gale-com.ezproxy.niagara.edu/ps/retrieve.do?tabID=T002&resultListType=RESULT_LIST&searchResultsType=SingleTab&retrievalId=11c7d45e-bc37-41be-855c-5558a890e714&hitCount=48935&searchType=BasicSearchForm&currentPosition=1&docId=GALE%7CA813057029&docType=Article&sort=Relevance&contentSegment=ZONE-MOD1&prodId=AONE&pageNum=1&contentSet=GALE%7CA813057029&searchId=R2&userGroupName=nysl_we_niagarau&inPS=true