// local reviews data
const reviews = [
  {
    id: 1,
    name: 'Sanji',
    job: 'Best Chef',
    img: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpaperaccess.com%2Ffull%2F3510921.jpg&f=1&nofb=1&ipt=c7c494207490160cfafff2d09f6a5e47316dcafa95c18b8e75c00d0986ec8dc3&ipo=images',
    text: "I'm baby meggings twee health goth +1. Bicycle rights tumeric chartreuse before they sold out chambray pop-up. Shaman humblebrag pickled coloring book salvia hoodie, cold-pressed four dollar toast everyday carry",
  },
  {
    id: 2,
    name: 'Roronoa Zoro',
    job: 'Greatest Swordsman',
    img: 'https://comicvine.gamespot.com/a/uploads/scale_medium/11143/111430001/7891642-sleepy-jhin-roronoa-zoro-portrait.jpg',
    text: 'Helvetica artisan kinfolk thundercats lumbersexual blue bottle. Disrupt glossier gastropub deep v vice franzen hell of brooklyn twee enamel pin fashion axe.photo booth jean shorts artisan narwhal.',
  },
  {
    id: 3,
    name: 'Nami',
    job: 'Navigator',
    img: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2F736x%2F4c%2F36%2F02%2F4c360208643933dfa96964e12efa836e.jpg&f=1&nofb=1&ipt=fdf3494e22a3e5005420f40f6cf90cc25f0bbf4aff4afa63e6847e7df55b2d27&ipo=images',
    text: 'Sriracha literally flexitarian irony, vape marfa unicorn. Glossier tattooed 8-bit, fixie waistcoat offal activated charcoal slow-carb marfa hell of pabst raclette post-ironic jianbing swag.',
  },
  {
    id: 4,
    name: 'Monkey D. Luffy',
    job: 'Pirate king',
    img: 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.iyxnN7jPo2zeJNJQ7Qyl-gHaHa%26pid%3DApi&f=1&ipt=ab60f11501e3589d975a59200ab4ed3f2203715b74a56174ee8899e511636cc6&ipo=images',
    text: 'Edison bulb put a bird on it humblebrag, marfa pok pok heirloom fashion axe cray stumptown venmo actually seitan. VHS farm-to-table schlitz, edison bulb pop-up 3 wolf moon tote bag street art shabby chic. ',
  },
];

//select items
const img = document.getElementById("person-img");
const author = document.getElementById("author");
const job = document.getElementById("job");
const info = document.getElementById("info");

const prevBtn = document.querySelector(".prev-btn");
const nextBtn = document.querySelector(".next-btn");
const randomBtn = document.querySelector(".random-btn");

let currItem = 3;

window.addEventListener("DOMContentLoaded", function() {
  const item = reviews[currItem];
  img.src = item.img;
  author.textContent = item.name;
  job.textContent = item.job;
  info.textContent = item.text;
});