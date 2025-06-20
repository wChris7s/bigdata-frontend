export interface ImgMetadata {
  alt_description: string;
  likes: number;
  downloads: number;
  urls: Urls;
  tags: Tag[];
}

export interface Urls {
  raw: string;
  full: string;
  regular: string;
  small: string;
  thumb: string;
  small_s3: string;
}

export interface Tag {
  type: string;
  title: string;
}
