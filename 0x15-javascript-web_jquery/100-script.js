document.onreadystatechange = function () {
  if (document.readyState === 'complete') {
    const header = document.querySelector('header');
    header.style.color = '#FF0000';
  }
};
