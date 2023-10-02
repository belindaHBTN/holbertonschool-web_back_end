import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  try {
    const photo = (await uploadPhoto()).body;
    const name = (await createUser());
    const { firstName, lastName } = name;
    console.log(photo, firstName, lastName);
  } catch (e) {
    console.log('Signup system offline');
  }
}
