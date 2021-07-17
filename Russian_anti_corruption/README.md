# Scrape

The scraping project requires the installation of [Splash](https://splash.readthedocs.io/en/stable/install.html)

1. Russia:
- President: [https://declarator.org/office/449](https://declarator.org/office/449)
- Federal Government: [http://declarator.org/office/453/](http://declarator.org/office/453/)
- Council of the Federation (upper house of parliament): [https://declarator.org/office/5/](https://declarator.org/office/5/)
- State Duma (lower house of parliament): [http://declarator.org/office/14/](http://declarator.org/office/14/)
Most of the scrape will yield results from 2015 - 2020. Depending on the particular scrape, 2010 and further back may not be available.
For State Duma and Council of Federation, due to their dynamic list, we had to go to their ajax URLs. Unfortunately, these URLs do not have workable nested HTML structures. As such, we had to resort to iterating over each member of each year (2015-2020), as otherwise, xpath would not work well. Feel free to devise a new methodology. Also, note that sometimes, you will just run into an URLError that is simply due to the URL returning a bad connection, in which case you will just have to run the script again.

For President and Federal Government, the procedure of the scrape starts with the URLs above (which do not have dynamic lists), collects all the years present and their associated URLs that lead to their data tables (these URLs must correspond with the text **Anti-corruption declaration**). From there, these associated URLs become the next taret for scraping: all members are scraped for relevant information, with most being contained in the **Show details** section.

