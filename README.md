# Python
const convertNumber = (number) => {
    const units = ['', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf'];
    const teens = ['dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize', 'dix-sept', 'dix-huit', 'dix-neuf'];
    const tens = ['', 'dix', 'vingt', 'trente', 'quarante', 'cinquante', 'soixante', 'soixante-dix', 'quatre-vingts', 'quatre-vingt-dix'];
    const hundreds = ['', 'cent', 'deux cents', 'trois cents', 'quatre cents', 'cinq cents', 'six cents', 'sept cents', 'huit cents', 'neuf cents'];

    if (number < 10) {
      return units[number];
    } else if (number < 20) {
      return teens[number - 10];
    } else if (number < 100) {
      return tens[Math.floor(number / 10)] + (number % 10 === 0 ? '' : '-' + units[number % 10]);
    } else if (number < 1000) {
      return hundreds[Math.floor(number / 100)] + (number % 100 === 0 ? '' : ' ' + convertNumber(number % 100));
    } else if (number < 1_000_000) {
      const thousand = Math.floor(number / 1000);
      const remainder = number % 1000;
      return (
        (thousand === 1 ? 'mille' : convertNumber(thousand) + ' mille') +
        (remainder === 0 ? '' : ' ' + convertNumber(remainder))
      );
    } else if (number < 1_000_000_000) {
      const million = Math.floor(number / 1_000_000);
      const remainder = number % 1_000_000;
      return (
        (million === 1 ? 'un million' : convertNumber(million) + ' millions') +
        (remainder === 0 ? '' : ' ' + convertNumber(remainder))
      );
    } else if (number < 1_000_000_000_000) {
      const milliard = Math.floor(number / 1_000_000_000);
      const remainder = number % 1_000_000_000;
      return (
        (milliard === 1 ? 'un milliard' : convertNumber(milliard) + ' milliards') +
        (remainder === 0 ? '' : ' ' + convertNumber(remainder))
      );
    } else {
      return 'Number too large';
    }
  };
  
