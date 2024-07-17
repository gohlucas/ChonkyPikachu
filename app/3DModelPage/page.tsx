"use client";
import React, { useEffect, useState } from 'react';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import * as THREE from 'three';

const ModelPage: React.FC = () => {
  const [selectedModel, setSelectedModel] = useState('/COM1 Basement.glb');

  useEffect(() => {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });

    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    const controls = new OrbitControls(camera, renderer.domElement);

    scene.background = new THREE.Color(0xffffff);

    const ambientLight = new THREE.AmbientLight(0xffffff, 1.0);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 1.8);
    directionalLight.position.set(0, 10, 0);
    scene.add(directionalLight);

    const loader = new GLTFLoader();

    let currentModel: THREE.Group | undefined;

    const loadModel = (modelPath: string) => {
      if (currentModel) {
        scene.remove(currentModel);
      }
      loader.load(modelPath, (gltf) => {
        currentModel = gltf.scene as THREE.Group;
        scene.add(currentModel);
      });
    };

    loadModel(selectedModel);

    camera.position.set(7.3589, 6.9258, 4.9583);
    camera.rotation.set(63.55 * (Math.PI / 180), 0, 46.69 * (Math.PI / 180));

    const animate = () => {
      requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
    };
    animate();

    const handleResize = () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
      document.body.removeChild(renderer.domElement);
    };
  }, [selectedModel]);

  return (
    <div>
      <select onChange={(e) => setSelectedModel(e.target.value)} value={selectedModel}>
        <option value="/COM1 Basement.glb">Basement</option>
        <option value="/COM1 Level 1.glb">First Floor</option>
        <option value="/COM1 Level 2.glb">Second Floor</option>
      </select>
    </div>
  );
};

export default ModelPage;