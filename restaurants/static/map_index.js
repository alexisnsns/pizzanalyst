mapboxgl.accessToken = document.getElementById('map').getAttribute('data-mapbox-access-token');

var  restaurantsAddresses = (document.getElementById('map').getAttribute('data-restaurants-addresses')).split(',');

var restaurantsNames = document.getElementById('map').getAttribute('data-restaurants-names').slice(2, -2).split(',');
restaurantsNames = restaurantsNames.map(item => item.trim().replace(/'/g, ''));

var restaurantsIndexes = document.getElementById('map').getAttribute('data-restaurants-indexes').slice(1, -1).split(',');
restaurantsIndexes = restaurantsIndexes.map(item => item.trim().replace(/'/g, ''));

var faviconUrl = document.getElementById('map').getAttribute('data-favicon-url');


var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/light-v11',
});

const bounds = new mapboxgl.LngLatBounds();

const fetchPromises = restaurantsAddresses.map(address =>
  fetch(`https://api.mapbox.com/geocoding/v5/mapbox.places/${encodeURIComponent(address)}.json?access_token=${mapboxgl.accessToken}`)
    .then(response => response.json())
);



Promise.all(fetchPromises)
  .then(dataArray => {
    dataArray.forEach((data, index) => {
      var coordinates = data.features[0].center;

      // Create custom pin for the marker
      var customPin = document.createElement('div');
      customPin.className = 'custom-marker';
      customPin.style.backgroundImage = `url("${faviconUrl}")`;

      console.log(restaurantsIndexes[index])
      var popupContent = '<h3><a href=" restaurants/' + restaurantsIndexes[index] + '">' + restaurantsNames[index] + '</a></h3>';

      var marker = new mapboxgl.Marker(customPin)
        .setLngLat(coordinates)
        .setPopup(new mapboxgl.Popup().setHTML(popupContent))
        .addTo(map);

      bounds.extend(coordinates);
    });

    map.fitBounds(bounds, { padding: 70, maxZoom: 15, duration: 0 });
  })
  .catch(error => {
    console.error('An error occurred:', error);
  });
