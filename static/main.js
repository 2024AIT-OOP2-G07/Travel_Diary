const map = new maplibregl.Map({
  container: "map",
  center: [137.3090958, 35.1323874],
  maxPitch: 85,
  zoom: 14,
  style: {
    version: 8,
    sources: {
      "background-osm-raster": {
        type: "raster",
        tiles: ["https://tile.openstreetmap.jp/styles/osm-bright-ja/{z}/{x}/{y}.png"],
        tileSize: 256,
        attribution:
          "<a href='https://www.openstreetmap.org/copyright' target='_blank'>© OpenStreetMap contributors</a>",
      },
    },
    layers: [
      {
        id: "background-osm-raster",
        type: "raster",
        source: "background-osm-raster",
      },
    ],
  },
});

map.on("load", async () => {
  const iconImage = await map.loadImage("../static/star.png");
  map.addImage("trip_point_icon", iconImage.data);
  map.addSource("trip_point", {
    type: "geojson",
    data: {
      type: "FeatureCollection",
      name: "point",
      crs: { type: "name", properties: { name: "urn:ogc:def:crs:OGC:1.3:CRS84" } },
      features: [
        {
          type: "Feature",
          properties: {
            day: "2024-11-23 18:00:00",
            name: "香嵐渓",
            address: "愛知県豊田市足助町飯盛",
            evaluation: 5,
            comment: "紅葉めちゃ綺麗！！！",
          },
          geometry: {
            type: "Point",
            coordinates: [137.3090958, 35.1323874],
          },
        },
      ],
    },
  });
  map.addLayer({
    id: "trip_point",
    type: "symbol",
    source: "trip_point",
    layout: {
      "icon-image": "trip_point_icon",
      "icon-size": 0.5,
    },
  });
});

map.on("click", "trip_point", (e) => {
  const coordinates = e.features[0].geometry.coordinates.slice();
  const message = `
    <strong>${e.features[0].properties.name}</strong>
    <p>${e.features[0].properties.address}</p>
    <p>評価: ${e.features[0].properties.evaluation}</p>
    <p>${e.features[0].properties.comment}</p>
    `;

  while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
    coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
  }
  new maplibregl.Popup({
    offset: 10,
    closeButton: false,
  })
    .setLngLat(coordinates)
    .setHTML(message)
    .addTo(map);
});
