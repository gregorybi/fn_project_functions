const fdk=require('@fnproject/fdk');

fdk.handle(function(input){
  let name = 'World !';
  let year = 0;
  let length_of_name = 0;
  
  if (input.name && input.year) {
    length_of_name = input.name.length;
    name = input.name + " !";
    year = 2022 - input.year;
  }
  
  console.log('\nInside Node Hello World function')
  return {'message': 'Hello ' + name, 'Your age is': year, 'The length of your name word is': length_of_name}
})
