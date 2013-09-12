Genres
======

Classification of genres used in the Paylogic API.

The keys represent descriptive genre codes. Genres have hierarchy and some genres have a reference
to a parent genre. There are also name translations provided for different language codes.

paylogic_genres.json:

.. code-block:: json

	{
	    "SPORTS": {
	        "ecc": "02", 
	        "name": {
	            "fr": "Sports", 
	            "en": "Sports", 
	            "nl": "Sports", 
	            "pt": "Sports", 
	            "de": "Sports", 
	            "tr": "Sports", 
	            "es": "Sports"
	        }
	    }, 
	    "SPORTS:RUGBY": {
	        "ecc": "02.06", 
	        "name": {
	            "fr": "Rugby",
	            "en": "Rugby",
	            "nl": "Rugby",
	            "pt": "Rugby",
	            "de": "Rugby", 
	            "tr": "Rugby", 
	            "es": "Rugby"
	        }, 
	        "parent": "SPORTS"
	    },
	    ...
	}
