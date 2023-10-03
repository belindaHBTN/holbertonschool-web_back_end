import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  const photoResult = await uploadPhoto();
  const userResult = await createUser();

  try {
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
