import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  const promise1 = uploadPhoto();
  const promise2 = createUser();

  return Promise.all([promise1, promise2]).then((results) => {
    console.log(`${results[0].body} ${results[1].firstName} ${results[1].lastName}`);
  }).catch(() => {
    console.log('Signup system offline');
  });
}
