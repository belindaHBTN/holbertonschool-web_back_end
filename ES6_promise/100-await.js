import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    const photoResult = await uploadPhoto();
    const userResult = await createUser();

    return {
      photo: photoResult,
      user: userResult,
    };
  } catch (e) {
    return {
      photo: null,
      user: null,
    };
  }
}
